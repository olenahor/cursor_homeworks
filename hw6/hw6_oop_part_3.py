from abc import abstractmethod, ABC


# 1. Implement class iterator for Fibonacci numbers https://en.wikipedia.org/wiki/Fibonacci_number
# Iterator get numbers of first Fibonacci numbers
class FibonacciNumbers:
    def __init__(self, max_count):
        self.max_count = max_count

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max_count:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib


for i in FibonacciNumbers(10):
    print(i)


# 2.* Implement generator for Fibonacci numbers

def fib_generator(n):
    a, b = 0, 1

    for i in range(n):
        yield a
        a, b = b, a + b


# 3. Write generator expression that returns square numbers of integers from 0 to 10
square_numbers_generator = (numb ** 2 for numb in range(11))

for elem in square_numbers_generator:
    print(elem)


# 4. Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.

class Laptop(ABC):
    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):
    def screen(self):
        return '14" diagonal FHD IPS BrightView'

    def keyboard(self):
        return 'US Layout with Backlight'

    def touchpad(self):
        return 'TouchPad zone, left TouchPad button, right TouchPad button'

    def webcam(self):
        return 'HP Wide Vision HD Camera with integrated dual array digital microphone'

    def ports(self):
        return '1 USB 3.1 Gen 1 Type-C™ (Data Transfer Only, 5 Gb/s signaling rate);' \
               '2 USB 3.1 Gen 1 Type-A (Data Transfer Only); 1 AC smart pin; 1 HDMI 1.4b;' \
               '1 headphone/microphone combo; 1 RJ-45'

    def dynamics(self):
        return 'B&O, dual speakers, HP Audio Boost'


test = HPLaptop()
print(test.webcam())


# 5. Create an abstract class for the Car with the next methods: drive, stop, open_door, close_door, turn_on_light,
# turn_off_light, enable_radio, disable_radio, where drive and stop will be predefined with some realization, all others
# should be abstract.
class Car:
    def drive(self):
        return 'Drive'

    def stop(self):
        return 'Stop'

    @abstractmethod
    def open_door(self):
        raise NotImplementedError

    @abstractmethod
    def close_door(self):
        raise NotImplementedError

    @abstractmethod
    def turn_on_light(self):
        raise NotImplementedError

    @abstractmethod
    def turn_off_light(self):
        raise NotImplementedError

    @abstractmethod
    def enable_radio(self):
        raise NotImplementedError

    @abstractmethod
    def disable_radio(self):
        raise NotImplementedError
