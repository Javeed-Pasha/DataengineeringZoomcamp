
variable "creds" {
  description = "my google credentials"
  default     = "<Path to credentials file >"

}

variable "project" {
  description = "Project"
  default     = "<project-id>"

}
variable "region" {
  description = "Project"
  default     = "us-west1-b"

}

variable "location" {
  description = "Project location"
  default     = "US"

}

variable "bq_dataset" {
  description = "my Biq query dataset name "
  default     = "bq_data_setname"

}

variable "gcs_storage_class" {

  description = "Bucket storage class"
  default     = "STANDARD"
}

variable "gcs_bucketname" {

  description = "Bucket name"
  default     = "forward-ace-first-bucket"
}
