# from urllib.parse import quote
import json
from langchain.document_loaders import YoutubeLoader


def test_ytb_download():
    # vid = 'L_Guz73e6fw'  # sam atman
    # vid = '13CZPWmke6A'  # Ilya Sutskever
    videos = {
        # 'andrian_karpathy': 'cdiD-9MMpb0',
        # 'yarn_lekun': 'SGzMElJ11Cc'
        # 'Max-Tegmark': 'VcVfceTsD0A',
        # 'Jordan Peterson': 'sY8aFSY2zv4',
        'Ilya-Sutskever-2:': 'SjhIlw3Iffs',
        # 'Elon3-zh': 'DxREm3s1scA',
    }
    for guest, vid in videos.items():
        loader = YoutubeLoader.from_youtube_url(f"https://www.youtube.com/watch?v={vid}", add_video_info=False)
        transcripts = loader.load()
        print(transcripts[0].metadata)
        with open(f'./ytb/{guest}.txt', 'w') as fp:
            fp.write(transcripts[0].page_content)
            # fp.write(transcripts[0].json())
        with open(f'./ytb/{guest}.json', 'w') as fp:
            json.dump(transcripts[0].json(), fp)


if __name__ == '__main__':
    test_ytb_download()
