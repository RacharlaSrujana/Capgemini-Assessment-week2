'''Create a class `Logger` with a method `log(message)`. Implement method overloading to log different message 
    types (`error`, `warning`, `info`).'''

class Logger:
    def log(self,message):
        if message=='error':
            print("Syntax error")
        elif message=='warning':
            print("Warning")
        elif message=='info':
            print("Information displayed")
logger=Logger()
logger.log(input("Enter message : "))