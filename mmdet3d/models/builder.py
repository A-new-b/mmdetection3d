from torch import nn

from mmdet.models.registry import (BACKBONES, DETECTORS, HEADS, LOSSES, NECKS,
                                   ROI_EXTRACTORS, SHARED_HEADS)
from ..utils import build_from_cfg
from .registry import FUSION_LAYERS, MIDDLE_ENCODERS, VOXEL_ENCODERS


def build(cfg, registry, default_args=None):
    if isinstance(cfg, list):
        modules = [
            build_from_cfg(cfg_, registry, default_args) for cfg_ in cfg
        ]
        return nn.Sequential(*modules)
    else:
        return build_from_cfg(cfg, registry, default_args)


def build_backbone(cfg):
    return build(cfg, BACKBONES)


def build_neck(cfg):
    return build(cfg, NECKS)


def build_roi_extractor(cfg):
    return build(cfg, ROI_EXTRACTORS)


def build_shared_head(cfg):
    return build(cfg, SHARED_HEADS)


def build_head(cfg):
    return build(cfg, HEADS)


def build_loss(cfg):
    return build(cfg, LOSSES)


def build_detector(cfg, train_cfg=None, test_cfg=None):
    return build(cfg, DETECTORS, dict(train_cfg=train_cfg, test_cfg=test_cfg))


def build_voxel_encoder(cfg):
    return build(cfg, VOXEL_ENCODERS)


def build_middle_encoder(cfg):
    return build(cfg, MIDDLE_ENCODERS)


def build_fusion_layer(cfg):
    return build(cfg, FUSION_LAYERS)
