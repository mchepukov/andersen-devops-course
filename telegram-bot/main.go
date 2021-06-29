package main

import (
	"fmt"
	"github.com/fsnotify/fsnotify"
	"github.com/spf13/viper"
	tb "gopkg.in/tucnak/telebot.v2"
	"log"
	"strconv"

	//"os"
	"time"
)

type Configurations struct {
	TELEGRAM_API_TOKEN string
	GITHUB_REPO        string
}

func main() {

	var configuration Configurations

	configViper := viper.New()
	tasksViper := viper.New()

	configViper.SetConfigName("config")
	configViper.SetConfigType("yaml")
	configViper.AddConfigPath(".")

	tasksViper.SetConfigName("tasks")
	tasksViper.SetConfigType("yaml")
	tasksViper.AddConfigPath(".")

	tasksViper.AutomaticEnv()

	err := configViper.ReadInConfig()
	if err != nil { // Handle errors reading the config file
		panic(fmt.Errorf("Fatal error config file: %w \n", err))
	}

	err = tasksViper.ReadInConfig()
	if err != nil { // Handle errors reading the config file
		panic(fmt.Errorf("Fatal error config file: %w \n", err))
	}

	tasksViper.WatchConfig()
	tasksViper.OnConfigChange(func(e fsnotify.Event) {
		fmt.Println("Config file changed:", e.Name)
	})

	err = configViper.Unmarshal(&configuration)
	if err != nil {
		fmt.Printf("Unable to decode into struct, %v", err)
	}

	// Start Telegram Bot
	TelegramApiToken := configuration.TELEGRAM_API_TOKEN

	b, err := tb.NewBot(tb.Settings{
		URL:    "",
		Token:  TelegramApiToken,
		Poller: &tb.LongPoller{Timeout: 10 * time.Second},
	})

	fmt.Println("Telegram BOT started...")

	if err != nil {
		log.Fatal(err)
		return
	}

	b.Handle("/git", func(m *tb.Message) {
		b.Send(m.Sender, configuration.GITHUB_REPO)
	})

	if err != nil {
		log.Println(err)
	}

	b.Handle("/tasks", func(m *tb.Message) {

		var message string
		countOfTasks := len(tasksViper.GetStringMapStringSlice("tasks"))
		for i := 1; i <= countOfTasks; i++ {
			task := tasksViper.GetStringMapString(fmt.Sprintf("tasks.task%d", i))

			message += fmt.Sprintf("Task %d: [%s](%s)\n", i, task["name"], task["url"])

		}

		b.Send(m.Sender, message, tb.NoPreview, tb.ParseMode(tb.ModeMarkdown))

	})

	if err != nil {
		log.Println(err)
	}

	b.Handle("/task", func(m *tb.Message) {

		var message string

		taskId, _ := strconv.Atoi(m.Payload)
		task := tasksViper.GetStringMapString(fmt.Sprintf("tasks.task%d", taskId))
		message = fmt.Sprintf(task["url"])

		b.Send(m.Sender, message, tb.NoPreview, tb.ParseMode(tb.ModeMarkdown))

	})

	b.Start()

}
