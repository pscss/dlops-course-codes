import torch


def test_torch_cuda():
    assert torch.cuda.is_available(), "CUDA should be available"


def test_torch_device():
    device = torch.device("cuda")
    tensor = torch.tensor([1.0], device=device)
    assert tensor.device.type == "cuda"
