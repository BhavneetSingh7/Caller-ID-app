from django.db import models

def normalize_phone_number():
    pass

class GlobalDB(models.Model):
    """
    Global Database includes all registered and personal contacts
    """
    phone_number = models.CharField(max_length=13, blank=False, null=True)
    country_code = models.CharField(max_length=4, blank=False, null=True)
    name = models.CharField(max_length=30, blank=False, null=True)
    email = models.EmailField(max_length=255, blank=True)
    is_registered = models.BooleanField(default=False)
    is_personal_contact = models.BooleanField(default=False)
    is_marked_as_spam = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.country_code + '-' +self.phone_number+ ': ' +self.name
    
    class Meta:
        ordering = [
            'id', 'name', 'is_registered', 'phone_number',
            'country_code', 'email', 'is_personal_contact', 'is_marked_as_spam'
        ]


class PersonalContact(models.Model):
    """
    Includes relation of a number as a personal contact of other number
    """
    personal_contact = models.ForeignKey(GlobalDB,related_name='Global2Personal', blank=False, on_delete=models.CASCADE)
    contact_of = models.ForeignKey(GlobalDB,related_name='Personal2Global', blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.personal_contact) + ' : ' + str(self.contact_of)


class SpamDB(models.Model):
    """
    Includes number of times a number is marked as spam
    """
    spam_phone_number = models.ForeignKey(GlobalDB,related_name='Global2Spam', blank=False, on_delete=models.CASCADE)
    marked_by = models.ForeignKey(GlobalDB,related_name='Spam2Global', blank=False, on_delete=models.CASCADE)
    marked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.spam_phone_number+ ': ' +self.marked_by
