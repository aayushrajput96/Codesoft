class password:
    
    def __init__(self, a):
        self.a = a

    def gen_pass(self):
        print('Password generated successfully...')

    print('*Password should be of 8 charachter')

    def validate(self):
        sp = False
        dig = False
        smc = False
        cpc = False
        if len(a) >= 8:
        
            for i in a:
                if i in '!@#$%_':
                    sp = True
                if '0' <= i <= '9': 
                    dig = True
                if 'a' <= i <= 'z':
                    smc = True 
                if 'A' <= i <= 'Z':
                    cpc = True
                    
            if sp and dig and smc and cpc:
                obj.gen_pass()     
            else:
                print('Password should contain !@#$%_,0-9,A-Z,a-z')
                    

        else:
            print('Length of password should be 8 or more')

a = input('Create your password: ')
obj = password(a)
obj.validate()
