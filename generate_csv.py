import pandas as pd
import os


if __name__ == "__main__":
    data_dir = "D:/fer/zavrsni_data/data_cpac/ABIDE_pcp/cpac/nofilt_noglobal"

    file_names = os.listdir(data_dir)

    file_ids = [name.replace("_func_preproc.nii.gz", "") for name in file_names]

    pheno_file_path = (
        "D:/fer/zavrsni_data/data_cpac/ABIDE_pcp/Phenotypic_V1_0b_preprocessed1.csv"
    )

    pheno_data = pd.read_csv(pheno_file_path)

    pheno_data = pheno_data[pheno_data["FILE_ID"].isin(file_ids)]

    pheno_data = pheno_data[["subject", "SITE_ID", "FILE_ID", "DX_GROUP"]]

    pheno_data["DX_GROUP"] = pheno_data["DX_GROUP"].replace({1: 0, 2: 1})

    pheno_data.to_csv(
        "D:/fer/zavrsni_data/data_cpac/ABIDE_pcp/abide_pheno.csv", index=False
    )
