'''
Usecase - It helps in solving problem like notifyme, where we need to notify users who
have to the service on data change (could be product availability)
'''
from __future__ import annotations
from abc import abstractmethod

class IStockObservable:
    @abstractmethod
    def add_observer(self, observer: INotificationAlertObserver):
        pass

    @abstractmethod
    def remove_observer(self, observer: INotificationAlertObserver):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

    @abstractmethod
    def setStockCount(self, x: int):
        pass

    @abstractmethod
    def getStockCount(self):
        pass

class IphoneObservable(IStockObservable):
    observerlist: INotificationAlertObserver = []
    stock_count : int = 0

    def add_observer(self, observer: INotificationAlertObserver):
        IphoneObservable.observerlist.append(observer)
    
    def remove_observer(self, observer: INotificationAlertObserver):
        try:
            IphoneObservable.observerlist.remove(observer)
        except ValueError:
            pass

    def notify_observers(self):
        for observer in IphoneObservable.observerlist:
            observer.update()
    
    def setStockCount(self, x: int) -> None:
        IphoneObservable.stock_count = IphoneObservable.stock_count + x

        # notifying all obserservers once stock is available
        if IphoneObservable.stock_count > 0:
            self.notify_observers()

        # deleting all observers once we have notified them about new stock
        for observer in IphoneObservable.observerlist:
            self.remove_observer(observer)
    
    def getStockCount(self):
        return IphoneObservable.stock_count

class INotificationAlertObserver:
    @abstractmethod
    def notify(self):
        pass

class EmailAlertObserver(INotificationAlertObserver):
    def __init__(self, email: str, observable: IStockObservable):
        self.email = email
        self.observable = observable

    def notify(self) -> None:
        self.__sendMail()
    
    # making sendmail accessible inside class only
    def __sendMail(self):
        print("sending mail")

class MobileAlertObserver(INotificationAlertObserver):
    def __init__(self, user: str, observable: IStockObservable):
        self.user = user
        self.observable = observable

    def notify(self) -> None:
        self.__sendMessageOnMobile()
    
    # making sendmessageonmobile accessible inside class only
    def __sendMessageOnMobile(self):
        print("sending mail")
