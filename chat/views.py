from django.core.checks import messages
from django.shortcuts import redirect, render
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create our views here.
def home(request):
  return render(request, 'index.html')

def room(request, room):
  username = request.GET.get('username')
  room_details = Room.objects.get(name=room)
  return render(request, 'room.html', {
    'username':username,
    'room':room,
    'room_details':room_details
  })

def checkview(request):
  room = request.POST['room_name']
  username = request.POST['username']

  if Room.objects.filter(name=room).exists():
    return redirect('/'+room+'/?username='+username)
  else:
    new_room = Room.objects.create(name=room)
    new_room.save()
    return redirect('/'+room+'/?username='+username)

def send(request):
  message = request.POST['message']
  username = request.POST['username']
  room_id = request.POST['room_id']

  new_message = Message.objects.create(text=message, user=username, room=room_id)
  new_message.save()
  return HttpResponse('Message Sent Successfully!')

def getMessages(request, room):
  room_details = Room.objects.get(name=room)
  messages = Message.objects.filter(room=room_details.id)
  return JsonResponse({'messages':list(messages.values())})