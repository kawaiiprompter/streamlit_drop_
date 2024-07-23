from io import BytesIO
from PIL import Image
import streamlit as st

def main():
    st.markdown("# DROP EXIF")
    img_file_buffer = st.file_uploader("ファイルを指定")
    if img_file_buffer is not None:
        with Image.open(img_file_buffer) as src:
            # 画像を表示
            st.image(src, caption=f"{img_file_buffer.name}", use_column_width=True)
            
            data = src.getdata()
            mode = src.mode
            size = src.size
            if "parameters" in src.info:
                parameters = src.info["parameters"]
                st.code(parameters, language="")
                                
                with Image.new(mode, size) as dst:
                    dst.putdata(data)
                    buf = BytesIO()
                    dst.save(buf, format="JPEG")
                    byte_im = buf.getvalue()
                    st.download_button(
                        label="Download image",
                        data=byte_im,
                        file_name=f"nometa_{img_file_buffer.name}",
                        mime="image/png"
                    )
            else:
                st.text("no exif")

if __name__ == "__main__":
    main()
