from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required

from datetime import datetime

from .models import Gallery, GalleryImage, GalleryComment

def index(request):
    galleries = Gallery.objects.all()
    return render(request, 'gallery/index.html', {'galleries':galleries})

def gallery(request, gallery_id):
    gallery = get_object_or_404(Gallery, slug=gallery_id)
    images = get_list_or_404(GalleryImage, gallery=gallery)
    return render(request, 'gallery/gallery.html', {'gallery': gallery, 'images': images})

def image(request, gallery_id, image_id):
    image_id = int(image_id);
    gallery = get_object_or_404(Gallery, slug=gallery_id)

    try:
        image = GalleryImage.objects.filter(gallery=gallery)[image_id-1]
    except IndexError:
        raise Http404("Image does not exist")

    total_images = GalleryImage.objects.filter(gallery=gallery).count()

    if (request.user.is_authenticated()):
        comments = GalleryComment.objects.filter(image=image).exclude(user=request.user).order_by('user', '-date').distinct('user')
        try:
            user_comment = GalleryComment.objects.filter(image=image, user=request.user).order_by('date').last()
        except GalleryComment.DoesNotExist:
            user_comment = None
    else:
        comments = GalleryComment.objects.filter(image=image).order_by('user', '-date').distinct('user')
        user_comment = None

    if image_id > 1:
        previous_page = image_id - 1
    else:
        previous_page = False
    if image_id < total_images:
        next_page = image_id + 1
    else:
        next_page = False

    return render(request, 'gallery/image.html', {
        'gallery': gallery,
        'image': image,
        'current_page': image_id,
        'next_page': next_page,
        'previous_page': previous_page,
        'total_pages': total_images,
        'comments': comments,
        'user_comment': user_comment,
        'current_user': request.user
        })

@login_required
def comment(request, gallery_id, image_id):
    image_id = int(image_id);
    gallery = get_object_or_404(Gallery, slug=gallery_id)

    try:
        image = GalleryImage.objects.filter(gallery=gallery)[image_id-1]
    except IndexError:
        raise Http404("Image does not exist")

    GalleryComment.objects.create(
        image = image,
        user = request.user,
        comment = request.POST['comment'],
        date = datetime.now()
    );

    if 'ajax' in request.POST:
        return JsonResponse({'success':'true'})
    else:
        return HttpResponseRedirect(reverse('gallery:image', args=(gallery_id, image_id)))