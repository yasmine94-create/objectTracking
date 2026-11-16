import cv2 
import numpy as np 
import  streamlit  as  st  
import tempfile

st.title('object tracking')


uploaded_file =  st.file_uploader('upload video' , type=['mp4', 'avi' ,'mov'])

if uploaded_file  is not None: 

    tf_file = tempfile.NamedTemporaryFile(delete=False)

    tf_file.write(uploaded_file.read())

    # st.write(uploaded_file.read())

    cap  =  cv2.VideoCapture(tf_file.name)

    st_frame  = st.empty()

    if  st.button('start  tracking'):

        background_remover  = cv2.createBackgroundSubtractorMOG2()
        
        while cap.isOpened() : 
            flag ,  frame  =  cap.read()
            if  not  flag : 
                break 

            masked_fr =  background_remover.apply(frame)
            #  contours 
            (contours  , _) =   cv2.findContours(masked_fr , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE )
            for  c  in contours : 
                if cv2.contourArea(c) > 500:   
                    x, y  , w , h   =  cv2.boundingRect(c)
                    cv2.rectangle(frame , (x,y) ,(x+w , y+h), (0,255,0) ,  2)

            frame_rgb =  cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
            st_frame.image(frame_rgb, caption='tracking object') 


        cap.release()
           