class Batch:
    """The internal data structure in Tianshou.
    
    Batch is a kind of supercharged array (of temporal data) stored individually in a
    (recursive) dictionary of object that can be either numpy array, torch tensor, or
    batch themselves. It is designed to make it extremely easily to access, manipulate
    and set partial view of the heterogeneous data conveniently.
    
    For a detailed description, please refer to :ref:`batch_concept`.
    """

    def __init__(
        self,
        batch_dict: Optional[Union[dict, "Batch", Sequence[Union[dict, "Batch"]],
                                   np.ndarray]] = None,
        copy: bool = False,
        **kwargs: Any,
    ) -> None:
        pass
