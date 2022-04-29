


def madLibGen(noun,verb,adverb,adjective,pronoun,conjuction):
    
    text1 = f"""{noun} is a collection of idioms.I am a {verb}. We are trying our {adverb} for the {verb}.{pronoun} is a collection of facts
    as we have to consider our {verb} {conjuction} the people have {adjective} experience."""
    print(text1)

noun = input("Enter Noun: ")
verb = input("Enter Verb: ")
adjective = input("Enter Adjective: ")
pronoun = input("Enter Pronoun: ")
adverb = input("Ente Adverb: ")
conjuction = input("Enter Conjuction: ")

madLibGen(noun, verb, adverb, adjective, pronoun, conjuction)