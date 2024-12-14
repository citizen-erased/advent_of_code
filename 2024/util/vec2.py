class vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, vec2):
            return vec2(self.x + other.x, self.y + other.y)
        return vec2(self.x + other, self.y + other)
    
    def __sub__(self, other):
        return vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, vec2):
            return vec2(self.x * other.x, self.y * other.y)
        return vec2(self.x * other, self.y * other)
    
    def __mod__(self, other):
        if isinstance(other, vec2):
            return vec2(self.x % other.x, self.y % other.y)
        return vec2(self.x % other, self.y % other)
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)
    
    def __le__(self, other):
        return (self.x, self.y) <= (other.x, other.y)
    
    def __gt__(self, other):
        return (self.x, self.y) > (other.x, other.y)
    
    def __ge__(self, other):
        return (self.x, self.y) >= (other.x, other.y)
    
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
    
    def __ne__(self, other):
        return (self.x, self.y) != (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))