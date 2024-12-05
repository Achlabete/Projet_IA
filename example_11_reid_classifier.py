#################################################################################
# Example of training classifier of a reider -> `trainReIDClassifier()`
#################################################################################

from pyppbox.standalone import trainReIDClassifier

def create_model_pkl():
    # Reider
    myreider={
        # 'ri_name': 'Torchreid', 
        # 'classifier_pkl': 'C:/pyppbox_v3/data/modules/torchreid/classifier/gta5_osnet_ain_ms_d_c.pkl', 
        # 'train_data': 'C:/pyppbox_v3/data/datasets/GTA_V_DATASET/body_128x256', 
        # 'model_name': 'osnet_ain_x1_0', 
        # 'model_path': 'C:/pyppbox_v3/data/modules/torchreid/models/torchreid/osnet_ain_ms_d_c.pth.tar', 
        # 'min_confidence': 0.35,
        # 'device': 'cuda'
        
        'ri_name': 'FaceNet',
        'gpu_mem': 0.585,
        'model_det': 'data/modules/facenet/models/det',
        'model_file': 'data/modules/facenet/models/20180402-114759/20180402-114759.pb',
        'classifier_pkl': 'prepface/abl_interface.pkl',
        # 'train_data': 'train_aligned_mix',
        'train_data': 'cropped_face',
        'batch_size': 1000,
        'min_confidence': 0.75,
        'yl_h_calibration': [-125, 75],
        'yl_w_calibration': [-55, 55]
    }

    trainReIDClassifier(
        reider=myreider
    )

    # The simplest way with internal config supposing everything is set the way you want, 
    # then you can simply import the `trainReIDClassifier` and call it directly; for example:
    #
    # >>> from pyppbox.standalone import trainReIDClassifier
    # >>> trainReIDClassifier()

