from jarvis_leaderboard.rebuild import (
    rebuild_pages,
    get_metric_value,
    get_results,
    get_all_dois,
    check_metadata_json_exists,
    check_run_sh_exists,
    check_at_least_one_csv_zip_exists,
    check_metadata_info_exists,
)


def test_check_errors():
    errors = rebuild_pages()
    assert len(errors) == 0


def test_get_results():
    names, vals = get_results(
        bench_name="AI-SinglePropertyPrediction-formation_energy_peratom-dft_3d-test-mae.csv.zip"
    )
    assert len(names) > 6


def test_sanity_check():
    p = check_metadata_json_exists()
    print("check_metadata_json_exists", p)
    assert len(p) == 0
    p = check_run_sh_exists()
    print("check_run_sh_exists", p)
    assert len(p) == 0
    p = check_metadata_info_exists()
    print("check_metadata_info_exists", p, len(p))
    assert len(p) == 0
    p = check_at_least_one_csv_zip_exists()
    print("check_at_least_one_csv_zip_exists", p)
    assert len(p) == 0
    p = get_all_dois()
    print("check all dois exist", len(p))


#test_sanity_check()
