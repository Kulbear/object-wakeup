import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import torch
import os
import argparse
from tqdm import tqdm
from pathlib import Path
from main import config
from utils import CheckpointIO
from main.utils.visualize import visualize_data

parser = argparse.ArgumentParser()
parser.add_argument('config', type=str, help='Path to config file.')

args = parser.parse_args()
cfg = config.load_config(args.config, 'demo.yaml')
device = torch.device("cuda")

out_dir = './demo_chair/'
generation_dir = './demo_chair/generation'
mesh_dir = os.path.join(generation_dir, 'meshes')
in_dir = os.path.join(generation_dir, 'input')
generation_vis_dir = os.path.join(generation_dir, 'vis')

Path(generation_dir).mkdir(exist_ok=True)
Path(mesh_dir).mkdir(exist_ok=True)
Path(in_dir).mkdir(exist_ok=True)
Path(generation_vis_dir).mkdir(exist_ok=True)
vis_n_outputs = 30

dataset = config.get_dataset('test', cfg, return_idx=True)
model = config.get_model(cfg, device=device, dataset=dataset)
model.eval()
generator = config.get_generator(model, cfg, device=device)
checkpoint_io = CheckpointIO('checkpoint', model=model)
checkpoint_io.load('model.pt')

generate_mesh = True

test_loader = torch.utils.data.DataLoader(
    dataset, batch_size=1, num_workers=0, shuffle=False)


for it, data in enumerate(tqdm(test_loader)):
    # Get index etc.
    idx = data['idx'].item()
    model_dict = {'model': str(idx), 'category': 'n/a'}

    # Generate outputs
    out_file_dict = {}
    modelpath = os.path.join(
        './demo_chair/', model_dict['model'],
        cfg['data']['watertight_file'])
    out_file_dict['gt'] = modelpath

    if generate_mesh:
        out = generator.generate_mesh(data)
        try:
            mesh, stats_dict = out
        except TypeError:
            mesh, stats_dict = out, {}

        # Write output
        mesh_out_file = os.path.join(mesh_dir, '%s.off' % model_dict['model'])
        mesh.export(mesh_out_file)
        out_file_dict['mesh'] = mesh_out_file


    inputs_path = os.path.join(in_dir, '%s.jpg' % model_dict['model'])
    inputs = data['inputs'].squeeze(0).cpu()
    visualize_data(inputs, 'img', inputs_path)
    out_file_dict['in'] = inputs_path