from pytube import YouTube

def on_complete(stream, filepath):
    print("Download complete")
    print(filepath)

def on_progress(stream, chunk, bytes_remaining):
    progress_string = f'({round(100 - (bytes_remaining/stream.filesize *100),2)}'
    print(progress_string)

link = input("YouTube link: ")
video_object = YouTube(link, on_complete_callback = on_complete, on_progress_callback = on_progress)

output_file = open("output.txt", "w")

print(f'title: {video_object.title}', file = output_file)
print(f'description: {video_object.description}', file = output_file)
print(f'author: {video_object.author}', file = output_file)
print(f'views: {video_object.views}', file = output_file)

