Foreign keys - go on the many side of the relationship, creates a reverse relationship of 
OTHERMODEL_set.all()
example: 
class Family(Model):
    name = models.CharField(max_length=50)
    
class Person(Model):
    name = models.CharField(max_length=50)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    
f = Family.objects.create(name='Sanchez')
p = Person.objects.create(name='rick', family=f)

p.family # will be the family
f.person_set.all() # will be all the person with family=f

OneToOneField

class Person(Model):
    name = models.CharField(max_length=50)
    
class Passport(Model):
    country = models.CharField(max_length=50)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    
p = Person.objects.create(name='Rick')
passport = Passport.objects.create(person=p, country='usa')

# the one to one field creates a reverse relationship on the other model by the original models name



passport.person 
p.passport


Many to Many

class Hobby(Model):
    name = models.CharField(max_length=50)
    
class Person(Model):
    name = models.CharField(max_length=50)
    hobbies = models.ManyToManyField(Hobby)


h = Hobby.objects.create(name='gaming')
p = Person.objects.get(id=1)
p.hobbies.add(h) # add specific hobbies
p.hobbies.remove(h) # remove specific hobbies
p.hobbies.clear() # removes all previous hobbies
p.hobbies.set([h]) # removes all previous hobbies and sets the list of hobbies provided

h.person_set.all() # all people with this hobby

