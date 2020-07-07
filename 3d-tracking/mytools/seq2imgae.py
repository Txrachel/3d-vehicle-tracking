
for seq in range(21):
    frame_idx = []
    name = str(seq).zfill(4)
    with open('./{}.txt'.format(name), 'r') as fo:
        lines = fo.readlines()
        for line in lines:
            frame_idx.append(int(line.split()[0]))
        max_frame_idx = max(frame_idx)
        min_frame_idx = min(frame_idx)
        for frame in range(min_frame_idx, max_frame_idx+1):
            for l in lines:
                if frame == int(l.split()[0]):
                    name_frame = str(frame).zfill(6)
                    with open('./{}/{}.txt'.format(name, name_frame), 'a+') as ff:
                        ff.write(l)
