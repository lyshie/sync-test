CC = gcc
CFLAGS = -O0

SRC_NESTED = jmp-nested.c
SRC_INTLV  = jmp-interleave.c
SRC_LINEAR = jmp-linear.c

BIN_NESTED = jmp-nested
BIN_INTLV  = jmp-interleave
BIN_LINEAR = jmp-linear

all: clean nested interleave linear

nested:
	$(CC) $(SRC_NESTED) $(CFLAGS) -o $(BIN_NESTED)

interleave:
	$(CC) $(SRC_INTLV) $(CFLAGS) -o $(BIN_INTLV)

linear:
	$(CC) $(SRC_LINEAR) $(CFLAGS) -o $(BIN_LINEAR)

clean:
	rm -f *.o $(BIN_NESTED) $(BIN_INTLV) $(BIN_LINEAR)
