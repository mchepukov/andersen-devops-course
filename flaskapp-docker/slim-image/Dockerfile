FROM amd64/debian:stable-slim AS build

RUN apt-get update
RUN apt-get install -y python3-pip python3-venv git upx binutils
RUN pip3 install pyinstaller patchelf-wrapper staticx
RUN git clone https://github.com/mchepukov/andersen-devops-course.git
RUN cd andersen-devops-course/python-flask-app/ && pip3 install -r requirements.txt && PYTHONOPTIMIZE=1  pyinstaller --add-data "templates:templates" --onefile app.py
RUN staticx --strip -l /lib/x86_64-linux-gnu/libgcc_s.so.1 /andersen-devops-course/python-flask-app/dist/app /andersen-devops-course/python-flask-app/dist/app-slim


FROM scratch
COPY --from=build /andersen-devops-course/python-flask-app/emoji_lib.txt /
COPY --from=build tmp /tmp
COPY --from=build /andersen-devops-course/python-flask-app/dist/app-slim /
ENTRYPOINT ["/app-slim"]