def test_apb_gpio_hidden_runner():
    import os
    from pathlib import Path
    from cocotb_tools.runner import get_runner

    sim = os.getenv("SIM", "icarus")
    proj_path = Path(__file__).resolve().parent.parent

    sources = [proj_path / "sources/apb_gpio_with_secret_toggle.sv"]

    runner = get_runner(sim)
    runner.build(
        sources=sources,
        hdl_toplevel="apb_gpio_with_secret_toggle",
        always=True,
    )
    runner.test(
        hdl_toplevel="apb_gpio_with_secret_toggle",
        test_module="apb_gpio_with_secret_toggle_test_hidden"
    )