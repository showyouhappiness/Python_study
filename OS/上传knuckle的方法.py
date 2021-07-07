import os

self.images_list = []
copy_path = r'E:\workImages\x5'
bucket = 'knuckle.debug'
self.copy_test(copy_path, bucket)


def copy_test(self, copied, bucket):
    if self.client.bucket_exists(bucket):
        f_log.LOGW("image bucket exists")
    else:
        self.client.make_bucket(bucket)
    if os.path.isdir(copied):
        # 被拷贝图片的列表
        copy_path_list = os.listdir(copied)
        if len(copy_path_list) > 5:
            self.images_list.clear()
            for copy_list in copy_path_list:
                # 判断这个列表是不是文件夹
                copy_detail_path = os.path.join(copied, copy_list)
                # 如果是文件夹，则再次打开它
                if os.path.isdir(copy_detail_path):
                    self.copy_test(copy_detail_path, bucket)
                else:
                    self.images_list.append(copy_detail_path)
                    if len(self.images_list) == 2:
                        images_filename = os.path.split(self.images_list[0])[1]
                        images_list_1 = int(os.path.splitext(self.images_list[1])[0][-2:])
                        images_list_0 = int(os.path.splitext(self.images_list[0])[0][-2:])
                        if int(os.path.splitext(self.images_list[0])[0][-2:]) >= 58:
                            images_list_0 = int(os.path.splitext(self.images_list[0])[0][-2:]) - 60
                        if images_list_1 - images_list_0 == 2:
                            print(self.client)
                            self.client.fput_object(bucket,
                                                    images_filename[:11] + "/" + images_filename,
                                                    copy_detail_path,
                                                    content_type='image/jpeg', metadata=None)
                            f_log.LOGW("{}".format(copy_detail_path))
                            self.images_list.pop(0)
                        else:
                            self.client.fput_object(bucket,
                                                    images_filename[:11] + "/" + images_filename,
                                                    copy_detail_path,
                                                    content_type='image/jpeg', metadata=None)
                            f_log.LOGW("{}".format(copy_detail_path))
                            break
        else:
            for copy_list in copy_path_list:
                copy_detail_path = os.path.join(copied, copy_list)
                self.client.fput_object(bucket, copy_list[:11] + "/" + copy_list,
                                        copy_detail_path,
                                        content_type='image/jpeg', metadata=None)
                f_log.LOGW("{}".format(copy_detail_path))
