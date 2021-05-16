class Address:
    def init(self,city,postCode):
        self.city = city
        self.postCode = postCode 
        
    def toString():
        return "City is "+city +", post code is "+postCode
        
class Accomodation :
    def init(self,name, Address):
        self.name = name
        self.address = Address
    
    def toString():
        return "Name is "+name+ ", "+address
    
    def getName():
        return name;
        
class Hotel(Accomodation):
    def init(self,name,Address,stars,beds):
        self.stars = stars
        self.beds = beds
        self.oneNight = 100;
        self.Accomdation = Accomodation(name,Address)
    
    def price():
        if beds > 2 and starts < 3:
           return beds*oneNight* stars*0.8
        elif beds >4 and stars>4:
           return beds*oneNight*stars*0.7
        else:
            return beds*oneNight
            
    def invoice():
	   return "Star is "+stars+ ", number of beds are "+beds+", total price is "+getPrice()+" TL"
	   
    def getPrice():
		return price()
		

def testFunction():
        address = Address("Istanbul",12345);
        hotel = Hotel("Grand Istanbul",address,3,2)
        print(hotel.invoice())
        print(hotel.getName())
        print(hotel.getPrice())
        
		
testFunction();