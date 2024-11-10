def multiply(byte1, byte2):
    result = 0
    for _ in range(8):
        if byte2 & 1:
            result ^= byte1
        
        carry = byte1 & 0x80
        byte1 = (byte1 << 1) & 0xFF
        if carry:
            byte1 ^= 0x1B
        
        byte2 >>= 1
    return result

byte1 = 0x57
byte2 = 0x83

result = multiply(byte1, byte2)

print(f"{byte1:02X} * {byte2:02X} = {result:02X}")
