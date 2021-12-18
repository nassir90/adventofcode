#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DEQUE_TYPE PacketData
#define print printf

typedef struct {
        size_t length;
        size_t effective_length;
        void* data;
} Deque;

typedef struct {
        int packet_type;
        int length_type;
        int length;
        int bits_read;
        Deque values;
} PacketData;

Deque
Deque_new() {
        return (Deque) {
                .length = 0,
                .effective_length = 0,
                .data = malloc(0)
        };
}

DEQUE_TYPE
Deque_pop(Deque* deque) {
        if (deque->effective_length != 0)
                deque->effective_length--;
        return ((DEQUE_TYPE*)deque->data)[deque->effective_length];
}

DEQUE_TYPE*
Deque_at(Deque* deque, int index) {
        if (index < 0)
                index += deque->effective_length;
        if (index < 0 || index >= deque->effective_length)
                return NULL;
        else
                return ((DEQUE_TYPE*)deque->data) + index;
}

void
Deque_append(Deque* deque, DEQUE_TYPE value) {
        if (++deque->effective_length > deque->length)
                deque->data = realloc(deque->data, sizeof(DEQUE_TYPE) * ++deque->length);
        *Deque_at(deque, -1) = value;
}

int to_decimal(char hex) {
        if (hex <= '9')
                return hex - 0x30;
        else
                return hex - 0x38;
}

int* to_bit_array(char* input) {
        size_t length = strlen(input);
        int* bits = malloc(length * 4 * 4);
        for (int i = 0; i < length * 4; i += 4) {
                int digit = to_decimal(input[i/4]);
                bits[i+3] = digit & 1;
                bits[i+2] = digit >> 1 & 1;
                bits[i+1] = digit >> 2 & 1;
                bits[i] = digit >> 3 & 1;
        }
        return bits;
}

int main() {
        FILE* file = fopen("example", "r");
        char* buffer = malloc(1);
        int step = 1;
        do {
                buffer = realloc(buffer, step * 64);
        } while (fgets(buffer + 63 * (step++ - 1), 64, file) != NULL);
        int* bits = to_bit_array(buffer);
        print("%s", buffer);
        free(buffer);
        fclose(file); // Forgetting to close the file will fuck shit up for reasons which I am presently unaware
        Deque packets = Deque_new();
        Deque_append(&packets, (PacketData){
                .packet_type = 0,
                .length_type = 1,
                .length = 1,
                .bits_read = 0,
                .values = Deque_new()
        });
        int current_bit = 0;
        while (packets.effective_length != 0) {
                int starting_bit = current_bit;
                PacketData* packet = Deque_at(&packets, -1);
                if (packet->length_type == 0 && packet->bits_read < packet->length || packet->length_type == 1 && packet->length > 0) {
                        packet->length -= 1;
                        int version = (bits[current_bit++] << 2) + (bits[current_bit++] << 1) + bits[current_bit++];
                        int type = (bits[current_bit++] << 2) + (bits[current_bit++] << 1) + bits[current_bit++];
                        if (type == 4) {
                                while (bits[current_bit++] != 0)
                                        current_bit += 4;
                                current_bit += 4;
                        } else {
                                int length_type = bits[current_bit++];
                                int bits_to_read = 15 - (length_type << 2 & 4);
                                int length = 0;
                                for (int i = bits_to_read - 1; i >= 0; --i) {
                                        print("%d ", bits[current_bit]);
                                        length += bits[current_bit++] << i;
                                }
                                print("\n");
                                Deque_append(&packets, (PacketData){
                                        .packet_type = type,
                                        .length_type = length_type,
                                        .length = length,
                                        .bits_read = 0,
                                        .values = Deque_new()
                                });
                        }
                        packet->bits_read += current_bit - starting_bit;
                } else {
                        PacketData last_packet = *packet;
                        Deque_pop(&packets);
                        if (packets.effective_length != 0)
                                Deque_at(&packets, -1)->bits_read += last_packet.bits_read;
                        free(last_packet.values.data);
                }
        }
}
