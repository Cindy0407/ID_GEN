import logging
from fastapi import APIRouter, Depends, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.api import model as public_model
from app.api.project.controller import model
from app.api.project.controller.number_gen import NumberGen
import gc

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__) 

router = APIRouter(prefix='/project',
                   tags=['tags'], responses={404: {"description": 'Not found'}})

@router.get("/gen_number/", response_model=public_model.Result, summary="身分證生成")
def get_gen_num(request: Request, params: model.Project = Depends(model.Project)):
    args_json = {
        "first_char": params.first_char,
        "gender": params.gender
    }
    redis_client = request.app.state.redis_client

    flag = None
    number_ctrl = None

    try:
        flag = True
        number_gen_ctrl = NumberGen()
        new_number_result = number_gen_ctrl.get_id(args_json, redis_client)
        logger.info(f"產生成功：{new_number_result}")
        return new_number_result
    except Exception as e:
        flag = False
        logger.error(f"產生身分證號時發生錯誤：{e}, {request}")
        raise
    finally:
        if flag:
            logger.info(request)
        
        del number_ctrl
        gc.collect()


