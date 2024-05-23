class Constants:
    BERT_BASE_UNCASED_DIM = 768

    WORD2VECTOR_DIM = 20 # pretrain on!!

    GGNN_ANNOTATION_DIM = WORD2VECTOR_DIM
    GGNN_OUTPUT_DIM = 32
    GGNN_STATE_DIM = 25  # state_dim must be no less than annotation_dim
    MAX_NODE_NUM = 15
    MAX_EDGE_NUM = 15
    GGNN_STEP_NUM = 10

    CG_MAX_NODE_NUM = 10

    CNN_INPUT_CHANNELS = 1
    CNN_COV_OUTPUT_CHANNELS = 16
    CNN_COV_MAX_OUTPUT = 1000
    ## CFG adj_matrix
    CNN_OUTPUT_DIM_CFG = 20
    ## CG adj_matrix
    CNN_OUTPUT_DIM_CG = 12

    MLP_HIDDEN_SIZE = 32

    EPOCHS = 30
    LR = 0.0005
    DEVICE = None

    W2VMODEL = None
    W2VEMBEDDING = None

    TRAIN_HOT_RATE = 0
    TEST_HOT_RATE = 0