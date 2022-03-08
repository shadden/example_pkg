CC=gcc
CFLAGS= -std=c99 -O3 -fPIC

SOURCES= example.c
OBJECTS=$(SOURCES:.c=.o)

all: $(SOURCES) libexample.so

%.o: %.c
	@echo "Compiling source file $< ..."
	$(CC) -c $(CFLAGS) -o $@ $<

libexample.so: $(OBJECTS)
	@echo ""
	@echo "Linking shared library $@ ..."
	$(CC) $(CFLAGS) -shared $(OBJECTS) -o $@

	@echo ""
	@echo "The shared library $< has been created successfully."

clean:
	@echo "Removing object files *.o ..."
	@-rm -f *.o
	@echo "Removing shared library libexample.so ..."
	@-rm -f *.so
