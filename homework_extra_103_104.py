import string

def rle_encode(value):
    """
    Implement run-length encoding and decoding.
    Run-length encoding (RLE) is a simple form of data compression, where runs (consecutive data elements) are
    replaced by just one data value and count.
    For example we can represent the original 53 characters with only 13.
    "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"  ->  "12WB12W3B24WB"
    RLE allows the original data to be perfectly reconstructed from the compressed data, which makes it a lossless data
    compression.
    "AABCCCDEEEE"  ->  "2AB3CD4E"  ->  "AABCCCDEEEE"
    For simplicity, you can assume that the unencoded string will only contain the letters A through Z (either lower or
    upper case) and whitespace. This way data to be encoded will never contain any numbers and numbers inside data
    to be decoded always represent the count for the following character.

    :param value: value to encode
    :return: encoded value
    """
    value += " "
    counter = 1
    encoded_string = ""
    for idx, char in enumerate(value[:-1]):
        if char != value[idx + 1]:
            if counter > 1:
                encoded_string += str(counter) + char
                counter = 1
            else:
                encoded_string += char
        else:
            counter += 1
    return encoded_string


def rle_decode(value):
    """
    Decodes string encoded with {rle_encode} function
    :param value: value to decode
    :return: decoded value
    """
    counter = ""
    decoded_string = ""
    for idx, char in enumerate(value):
        if char in string.digits:
            counter += char
        else:
            if counter != "":
                decoded_string += char * int(counter)
                counter = ""
            else:
                decoded_string += char
    return decoded_string


txt = "WWWWWWWWwwWWWWBWWWWWWW WWWWWBBbBWWWWWWWWWWW   WWWWWWWWWWWWWBB"
print(txt)
print(rle_encode(txt))
print(rle_decode(rle_encode(txt)))
