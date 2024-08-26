import wave
import numpy as np

# WAV 파일 열기
with wave.open('소리테스트.wav', 'rb') as wav_file:  # 'output_file.wav'는 파일 경로입니다.
    # 파라미터 추출
    num_channels = wav_file.getnchannels()  # 채널 수 (모노/스테레오)
    sample_width = wav_file.getsampwidth()  # 샘플의 바이트 수
    num_frames = wav_file.getnframes()      # 전체 프레임 수

    # 모든 프레임 읽기
    frames = wav_file.readframes(num_frames)

    # numpy 배열로 변환
    if sample_width == 1:
        data = np.frombuffer(frames, dtype=np.uint8) - 128
    elif sample_width == 2:
        data = np.frombuffer(frames, dtype=np.int16)
    else:
        raise ValueError("지원하지 않는 샘플 폭입니다.")

    # 스테레오일 경우 채널별로 분리
    if num_channels > 1:
        data = np.reshape(data, (-1, num_channels))

# 쉼표로 구분된 데이터 리스트를 파일에 저장
with open("output_data.txt", "w") as f:
    f.write("[")
    f.write(", ".join(map(str, data.flatten())))
    f.write("]")

print("진폭 데이터가 [1, 2, 3, ...] 형식으로 output_data.txt 파일에 저장되었습니다.")
