# super-duper ucet
class Ucet:

    def __init__(self, zustatek: int =0):
        self.zustatek : float = zustatek

    def pridej(self, kolik: float) -> None:
        self.zustatek += kolik


if __name__ == "__main__":
    ucet = Ucet(101)
    ucet.pridej(200)
    print(ucet.zustatek)
