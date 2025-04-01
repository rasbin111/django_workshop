from .models import Profile


def create_profile(backend, user, *args, **kwargs):
    """
    Create user profile for social authentication
    """
    if backend.name == 'google-oauth2':
        # Create or get profile
        profile, created = Profile.objects.get_or_create(user=user)
        if created:
            # Get the user's data from the social auth response
            response = kwargs.get('response', {})
            
            # Update profile with additional information if available
            if response.get('picture'):
                # You might want to download and save the profile picture here
                pass
                
            # You can add more fields from the response as needed
            # For example:
            # if response.get('birthday'):
            #     profile.date_of_birth = response['birthday']
            
            profile.save()

