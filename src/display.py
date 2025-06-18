class Display:
    """
    For displaying objects.
    """
    def __init__(self,
                 id,
                 car_park,
                 message = "",
                 is_on = False
                 ):
        self.id = id
        self.car_park = car_park
        self.message = message
        self.is_on = is_on


    def __str__(self):
        return f"{self.id}: Display is {'on' if self.is_on else 'off'}"


    def update(self, data):
        if "message" in data:
            self.message = data["message"]