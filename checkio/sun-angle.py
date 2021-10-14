from typing import Union


def sun_angle(time: str) -> Union[int, str]:
    angle = (int(time.split(":")[0])-6) * 15 + int(time.split(":")[1]) * 0.25
    if angle < 0 or angle > 180:        # we delete the negative angles        
        return "I don't see the sun!" 
    # replace this for solution
    return angle


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
