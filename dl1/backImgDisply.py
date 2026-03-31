# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 19:22:16 2026

@author: lcarr
"""

import os
import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def get_desktop_image_path() -> str:
    """
    현재 사용자 바탕화면의 background.png 경로를 반환합니다.
    """
    try:
        home_dir = os.path.expanduser("~")  # C:\Users\<username>
        print(f"바탕화면 경로: {home_dir}")
        desktop_dir = os.path.join(home_dir, "OneDrive", "바탕 화면")
        print(f"바탕화면 경로2: {desktop_dir}")
        image_path = os.path.join(desktop_dir, "background.png")
        return image_path
    except Exception as error:
        # 경로 계산 실패 시 에러 메시지 출력 후 종료
        print(f"바탕화면 경로 계산 중 오류가 발생했습니다: {error}")
        sys.exit(1)
def show_background_image() -> None:
    """
    바탕화면의 background.png 파일을 읽어서 matplotlib으로 출력합니다.
    """
    try:
        image_path = get_desktop_image_path()
        if not os.path.exists(image_path):
            print(f"이미지 파일을 찾을 수 없습니다: {image_path}")
            print("background.png 파일이 실제로 바탕화면에 있는지 확인해주세요.")
            return
        # 이미지 읽기
        image = mpimg.imread(image_path)
        # 이미지 출력
        plt.figure(figsize=(8, 6))
        plt.imshow(image)
        plt.axis("off")  # 축 숨기기
        plt.title("Desktop background.png", fontsize=14)
        plt.tight_layout()
        plt.show()
    except Exception as error:
        print(f"이미지 출력 중 오류가 발생했습니다: {error}")
if __name__ == "__main__":
    show_background_image()