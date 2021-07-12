from mmdet.apis import (inference_detector,
                        init_detector, show_result_pyplot)
import json
import mmcv
import numpy as np
from PIL import Image
from pathlib import Path

class FileIO:
    def load_image(self, options={}):
        file_name = options["file_name"]
        dtype = options["dtype"]

        img = Image.open(file_name)
        img.load()
        data = np.asarray(img, dtype=dtype)
        return data

    def save_image(self, data, options={}):
        file_name = options["file_name"]
        dtype = options["dtype"]
        start_pixel = options["start_pixel"]
        end_pixel = options["end_pixel"]

        img = Image.fromarray(
            np.asarray(
                np.clip(data, start_pixel, end_pixel), dtype=dtype
            )
        )
        img.save(file_name)

class Predict(FileIO):
    def load(self, args):
        '''
            정의된 model 및 dict load
        '''
        result = init_detector(args["config"], args["checkpoint"], device=args["device"])
        return result

    def action(self, model, args):
        '''
            예측 수행
        '''
        result = inference_detector(model, args["input"])

        return result

    def show(self, model, args, predict):
        '''
            결과 확인(원본)
        '''
        show_result_pyplot(model, args["input"], predict, args["score_thr"])

    def save(self, model, args, predict):
        '''
            결과 저장(score보다 클때)
        '''
        model.show_result(args["input"], predict, out_file=args["output"], score_thr=args["score_thr"])

    def json(self, model, args):
        '''
            임계치 값 기준 
        '''
        img = args["input"]
        out = args["output"]
        result = args["predict"]
        score_thr = args["score_thr"]

        img = mmcv.imread(img)
        img = img.copy()
        if isinstance(result, tuple):
            bbox_result, segm_result = result
            if isinstance(segm_result, tuple):
                segm_result = segm_result[0]
        else:
            bbox_result, segm_result = result, None
        bboxes = np.vstack(bbox_result)
        labels = [
            np.full(bbox.shape[0], i, dtype=np.int32)
            for i, bbox in enumerate(bbox_result)
        ]
        labels = np.concatenate(labels)

        jsons = []
        
        count = 1
        for box,label in zip(bboxes,labels):
            label_text = model.CLASSES[label]
            bbox = box.astype(np.float32)
            box = bbox[0:4]
            score = bbox[4]

            if score > score_thr:
                jsons.append(
                    {
                        'id':int(count),
                        'key':int(label),
                        'label':str(label_text),
                        'box':box.tolist(),
                        'score':float(score*100)
                    }
                )
                count += 1
        
        predict_json_path = f"{out}.json"
        predict_jsons = jsons
        with open(predict_json_path, "w") as json_file:
            json.dump(predict_jsons, json_file)

        return predict_json_path, predict_jsons

    def run(self, options={}):
        try:
            dir = Path(__file__).resolve().parent

            model_args = {
                "device":"cuda:0",
                "config":f"{dir}\\configs\\{options['model_root']}\\{options['model_name']}.py",
                "checkpoint":f"{dir}\\checkpoints\\{options['model_name']}.pth",
            }

            image_args = {
                "input":f"{dir}\\data\\{options['input_file_name']}",
                "output":f"{dir}\\data\\{options['predict_file_name']}",
                "score_thr":0.5,
            }
            
            model = self.load(model_args)
            result = self.action(model, image_args)
            image_args["predict"] = result
            self.save(model, image_args, result)

            input_image_path = f"{dir}\\data\\{options['input_file_name']}"
            predict_image_path = f"{dir}\\data\\{options['predict_file_name']}"
            predict_json_path, predict_jsons = self.json(model, image_args)
            
        except Exception as ex:
            print(ex)

        return input_image_path, predict_image_path, predict_json_path, predict_jsons


def sample():
    predict = Predict()

    model_args = {
        "device":"cuda:0",
        "config":"./configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py",
        "checkpoint":"./checkpoints/faster_rcnn_r50_fpn_1x_coco.pth",
    }

    image_args = {
        "input":"./inputs/norangE.jpg",
        "output":"./outputs/norangE.jpg",
        "score_thr":0.8,
    }

    model = predict.load(model_args)

    result = predict.action(model, image_args)
    
    #predict.show(model,arg,result)
    image_args["predict"] = result
    predict.save(model, image_args, result)

    input_image_options = {
        "file_name" : f"./inputs/norangE.jpg",
        "dtype" : "uint8"
    }
    input_image = predict.load_image(input_image_options)

    predict_image_options = {
        "file_name" : f"./outputs/norangE.jpg",
        "dtype" : "uint8"
    }
    predict_image = predict.load_image(predict_image_options)
    

    print(input_image.shape)
    print(predict_image.shape)
    
    return input_image, predict_image


predict = Predict()
