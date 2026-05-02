def decrypt_payload(encrypted_payload: bytes) -> bytes:
    if not encrypted_payload:
        raise ValueError("empty payload")

    key_len = encrypted_payload[0]
    buffer_size = len(encrypted_payload)

    if not (1 <= key_len <= 64):
        raise ValueError(f"invalid key length: {key_len}")

    if key_len + 1 >= buffer_size:
        raise ValueError("payload does not contain encrypted data")

    key = encrypted_payload[1:1 + key_len]
    encrypted_data = bytearray(encrypted_payload[1 + key_len:])

    print(f"decrypt: kl={key_len} data_sz={len(encrypted_data)}")

    for i in range(len(encrypted_data)):
        encrypted_data[i] ^= key[i % key_len]

    if len(encrypted_data) >= 2:
        print(f"plain[0..1]={encrypted_data[0]:02X}{encrypted_data[1]:02X}")
    elif len(encrypted_data) == 1:
        print(f"plain[0]={encrypted_data[0]:02X}")

    return bytes(encrypted_data)

data = open("Addon3_encrypted_payload.bin", "rb").read()
decrypted_data = decrypt_payload(data)
open("Addon3_decrypted_payload.bin","wb").write(decrypted_data)
