import os
import subprocess

def gif_to_mp4(input_path, output_path): #ffmpeg
    try:
        # ffmpeg 명령어 생성
        command = [
            "ffmpeg",
            "-i", input_path,  # 입력 GIF 파일 경로
            "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2",  # 가로 및 세로 크기를 2의 배수로 조정
            "-c:v", "libx264",  # 비디오 코덱 설정
            "-preset", "slow",  # 변환 품질 설정
            "-pix_fmt", "yuv420p",  # 픽셀 형식 설정
            output_path  # 출력 MP4 파일 경로
        ]

        # ffmpeg 실행
        subprocess.run(command, check=True)
        print("Conversion completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")

def batch_convert_gif_to_mp4(input_folder, output_folder):
    #로드
    gif_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".gif")]

    #없음 생성
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for gif_file in gif_files:
        #변환
        gif_path = os.path.join(input_folder, gif_file)
        mp4_file = gif_file[:-4] + ".mp4"  # 확장자 변경
        mp4_path = os.path.join(output_folder, mp4_file)

        gif_to_mp4(gif_path, mp4_path)

#address
input_folder = " "
output_folder = " "

batch_convert_gif_to_mp4(input_folder, output_folder)
