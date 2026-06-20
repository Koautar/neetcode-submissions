class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()  # to enregistre les valeur unique 
        for email in emails :
            local , domain = email.split("@")
            local = local.split("+")[0]# on prend l'element position 0 dans l aliste psq la fonction splite renvoie deux element
            local = local.replace('.','') 
            unique.add((local,domain)) # add prend one argument 

        return len(unique)
        