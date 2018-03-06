def get_valid_input(input_string, valid_options):
    """
    Waits for the valid input
    :param input_string: prompt for an input
    :param valid_options: options for a response
    :return: a valid response
    """
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Property:
    """
    Representation of a real estate property
    Attributes:
        :square_feet: an area of a property
        :beds: number of bedrooms
        :baths: number of bathrooms
    """
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        Displays attributes of a Property class
        :return: a print of a general information about a property
        """
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """
        A prompt for an information about a property
        :return: a dicrionary with names of attr as key and info as value
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))
    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    """
    A sub-class of Property, representation of an apartment
    Attributes:
        :balcony: is the balcony there
        :laundry: is the laundry there
    """
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        Displays attributes of an Apartment class
        :return: a print of a general info about property and additional information about an apartment
        """
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def prompt_init():
        """
        A prompt for an information about an apartment
        :return: a dictionary with name as key and answer as value
        """
        parent_init = Property.prompt_init()
        laundry = get_valid_input("What laundry facilities does the property have? ",
                                  Apartment.valid_laundries)
        balcony = get_valid_input("Does the property have a balcony? ",
                                  Apartment.valid_balconies)
        parent_init.update({"laundry": laundry, "balcony": balcony})
        return parent_init
    prompt_init = staticmethod(prompt_init)


class House(Property):
    """
    A representation of a house, a sub-class of Property
    Attributes:
        :garage: an information about a garage
        :fence: an information about a fence
    """
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        Displays attributes of an House class
        :return: a print of a general info about property and additional information about a house
        """
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        """
        A prompt for an additional information about a house
        :return: a dictionary with name as key and answer as value
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ", House.valid_fenced)
        garage = get_valid_input("Is there a garage? ", House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({"fenced": fenced, "garage": garage,
                            "num_stories": num_stories})
        return parent_init
    prompt_init = staticmethod(prompt_init)


class Purchase:
    """
    An information about a purchase of a property
    Attributes:
        :price: a price of a unit
        :taxes: an amount of taxes
    """
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        Displays attributes of an Purchase class
        :return: a print of a general info about a purchase
        """
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        """
         A prompt for an additional information about a purchase
        :return: a dictionary with name as key and info as value
        """
        return dict(price=input("What is the selling price? "),
                    taxes=input("What are the estimated taxes? "))

    prompt_init = staticmethod(prompt_init)


class Rental:
    """
    An representation of a rental of a property
    Attributes:
        :rent: an amount of monthly rent
        :utilities: additional utilities
    """
    def __init__(self, furnished='', utilities='', rent='', **kwargs):

        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        Displays attributes of an Rental class
        :return: a print of a general info about a rental
        """
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """
        A prompt for an additional information about a rental
        :return: a dictionary with name as key and info as value
        """
        return dict(rent=input("What is the monthly rent? "),
                    utilities=input("What are the estimated utilities? "),
                    furnished=get_valid_input("Is the property furnished? ",
                                              ("yes", "no")))

    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    """
    A representation of a rented house, subclass of Rental and House classes
    """
    def prompt_init():
        """
        Calls prompt for input from its parent classes(House and Rental)
        :return a dict with all information
        """
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    """
    A representation of a rented apartment, subclass of Rental and Apartment classes
    """
    def prompt_init():
        """
        Calls prompt for input from its parent classes(Apartment and Rental)
        :return a dict with all information
        """
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    """
    A representation of a purchased apartment, subclass of Purchase and Apartment classes
    """
    def prompt_init():
        """
        Calls prompt for input from its parent classes(Apartment and Purchase)
        :return a dict with all information
        """
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    """
    A representation of a purchased house, subclass of Purchase and House classes
    """
    def prompt_init():
        """
        Calls prompt for input from its parent classes(Apartment and Purchase)
        :return a dict with all information
        """
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class Agent:
    """
    A representation of a real estate agent
    Attributes:
        :property_list: a list of all properties-objects
        :type_map: a class varible, for choosing a right class of a property
    """
    def __init__(self):
        """
        Initializes a property_list attribute
        """
        self.property_list = []

    def display_properties(self):
        """
        Displays information using a function from a PropertyClass respectively
        :return: an information about all the properties of this object printed
        """
        for property in self.property_list:
            property.display()
    type_map = {("house", "rental"): HouseRental,
                ("house", "purchase"): HousePurchase,
                ("apartment", "rental"): ApartmentRental,
                ("apartment", "purchase"): ApartmentPurchase}

    def add_property(self):
        """
        Determines a class of property and
        prompts an information for it
        :return: adds a property to a list of all object's properties
        """
        property_type = get_valid_input("What type of property? ",
                                        ("house", "apartment")).lower()
        payment_type = get_valid_input("What payment type? ",
                                       ("purchase", "rental")).lower()
        PropertyClass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        #print(init_args)
        self.property_list.append(PropertyClass(**init_args))

    def __str__(self):
        """
        Prints overall information about agent's properties
        """
        house_rent, house_purchase, ap_rent, ap_purchase =0,0,0,0
        for property in self.property_list:
            if isinstance(property, HouseRental):
                house_rent +=1
            elif isinstance(property, HousePurchase):
                house_purchase +=1
            elif isinstance(property, ApartmentPurchase):
                ap_purchase += 1
            else:
                ap_rent +=1
        print("""This agent has {} houses for sale and {} houses for rent, as well as
        {} apartments for sale and {} apartments for rent""")
        

