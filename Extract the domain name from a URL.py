def domain_name(url) :
    if "http" in url :
        if "www" in url :
            string = []
            for i in range(0,len(url)) :
                if url[i] == "." :
                    string.append(i)
            domain = url[(string[0] +1):string[1]]  
            return domain                    
        else :
            dot = url.find(".")
            slash = url.find("/")
            domain = url[(slash+2):dot]
            return domain
    else :
         if "www" in url :
            string = []
            for i in range(0,len(url)) :
                if url[i] == "." :
                    string.append(i)
            domain = url[(string[0] +1):string[1]]  
            return domain
         else :
            dot = url.find(".")
            domain = url[:dot]
            return domain

