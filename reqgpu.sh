#!/bin/env bash

salloc --nodes=1 --gres=gpu:2 --time=02:30:00 --mem=0 --cpus-per-task=32

