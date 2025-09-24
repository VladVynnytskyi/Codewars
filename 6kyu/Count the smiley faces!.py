def count_smileys(arr):
    smiley = 0
    correct = [':)',':-)',':~)', ';)', ';-)',';~D', ':D',':-D', ':~D', ';D', ';-D', ';~D']
    for face in arr:
        if face in correct:
            smiley += 1
    return smiley

#or 

def count_smileys(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]

    smiley_count = 0

    for face in arr:
        # Перевіряємо довжину (може бути 2 або 3 символи)
        if len(face) == 2:
            eye, mouth = face[0], face[1]
            if eye in eyes and mouth in mouths:
                smiley_count += 1

        elif len(face) == 3:
            eye, nose, mouth = face[0], face[1], face[2]
            if eye in eyes and nose in noses and mouth in mouths:
                smiley_count += 1

        # Якщо більше 3 символів — це не смайлик

    return smiley_count
