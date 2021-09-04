"""Import modules information"""

from abc import ABCMeta, abstractmethod


class DirectToHomeService(metaclass=ABCMeta):
    """Definition of abstract class DirectToHomeService"""
    __counter=101
    def __init__(self,consumer_name):
        """Parameterized constructor"""
        self.__consumer_name=consumer_name
        self.__consumer_number=DirectToHomeService.__counter
        DirectToHomeService.__counter+=1

    def get_consumer_number(self):
        """Getter method for consumer number"""
        return self.__consumer_number

    def get_consumer_name(self):
        """Getter method for consumer name"""
        return self.__consumer_name

    @abstractmethod
    def calculate_monthly_rent(self):
        """Abstract method definition"""
        pass


class BasePackage(DirectToHomeService):
    """Definition of BasePackage class inheriting from abstract class DirectToHomeService"""
    def __init__(self,consumer_name,base_pack_name,subscription_period):
        """Parameterized constructor"""
        self.__base_pack_name=base_pack_name
        self.__subscription_period=subscription_period
        super().__init__(consumer_name)

    def get_base_pack_name(self):
        """Getter method for base pack name"""
        return self.__base_pack_name

    def get_subscription_period(self):
        """Getter method for subscription period"""
        return self.__subscription_period

    def validate_base_pack_name(self):
        """Definition of method for validation of base pack name"""
        if(self.__base_pack_name=="Silver" or self.__base_pack_name=="Gold"
or self.__base_pack_name=="Platinum"):
            return True
        self.__base_pack_name="Silver"
        print("Base package name is incorrect, set to Silver or Gold or Platinum")
        return False #True

    def calculate_monthly_rent(self):
        """Definition of method for calculating monthly rent"""
        if self.__subscription_period>=1 and self.__subscription_period<=24:
            if self.validate_base_pack_name() is True:
                if self.__subscription_period>12:
                    if self.__base_pack_name=="Silver":
                        discount=350
                        monthly_rent=350
                    elif self.__base_pack_name=="Gold":
                        discount=440
                        monthly_rent=440
                    elif self.__base_pack_name=="Platinum":
                        discount=560
                        monthly_rent=560
                else:
                    if self.__base_pack_name=="Silver":
                        discount=0
                        monthly_rent=350
                    elif self.__base_pack_name=="Gold":
                        discount=0
                        monthly_rent=440
                    elif self.__base_pack_name=="Platinum":
                        discount=0
                        monthly_rent=560
                final = (monthly_rent*self.__subscription_period)-discount
                final_monthly_rent = final/self.__subscription_period
                return final_monthly_rent
            return -1
        return -1
