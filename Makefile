PYC=pyinstaller
SRCS=app.py
ICON=./imgs/app/wave.icns
TARGET=wave.app
PYFLAGS=--onefile -n $(TARGET) -p $(VIRTUAL_ENV) --icon $(ICON) --clean

all:
	$(PYC) $(PYFLAGS) $(SRCS)

.PHONY: clean run

clean:
	$(RM) -r dist/ build/ $(TARGET).spec

run:
	./dist/$(TARGET)