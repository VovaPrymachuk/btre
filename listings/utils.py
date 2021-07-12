def photoList(listings):
        internal_photos = []
        for i in range(1, 6):
            if getattr(listings, 'photo_%d' % i):
                photo = getattr(listings, 'photo_%d' % i)
                internal_photos.append(photo)
        return internal_photos
