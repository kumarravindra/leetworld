# https://www.youtube.com/watch?v=TzIuVm1npgw&ab_channel=BinaryBeast
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

def song_divisible_60(times):
    # declare 60 elements array with 0 initial value
    elements = [0]*60
    pairs = 0

    for i in times:

        # -ve will give the value which we need for modulus like -100 % 60 = 20 but 100 % 60 will give 40
        pairs += elements[-i % 60]
        # keep modify element array
        elements[i % 60] += 1
    return pairs

our_time = [30, 20, 150, 100, 40]
print(song_divisible_60(our_time))



