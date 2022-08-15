from main.network.encoder import conv

encoder_dict = {
    'simple_conv': conv.ConvEncoder,
    'resnet18': conv.Resnet18,
    'vit_light': conv.ViTLight,
    'vit_large': conv.ViTLarge,
}
